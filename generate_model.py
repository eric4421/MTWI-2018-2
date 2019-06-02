# -*- coding: utf-8 -*-

"""
Generate revised VGG16 model.
"""

import sys
import torch
import torchvision.models as models
import net.network as Net

# generate revised VGG16 pretrained model
def generate_VGG_16_model(network, output_path):
    vgg_16 = models.vgg16(pretrained=False)
    #print(vgg_16)

    # load VGG16 pretrained model
    vgg_16.load_state_dict(torch.load('./model/vgg16-397923af.pth'))

    # generate
    pretrained_dict = vgg_16.state_dict()
    model_dict = network.state_dict()
    check_list = [[], []]
    for i in range((2 + 2 + 3 + 3 + 3) * 2):
        check_list[0].append(list(pretrained_dict.keys())[i])
        check_list[1].append(list(model_dict.keys())[i])
    backbone_dict = {}
    for j in range((2 + 2 + 3 + 3 + 3) * 2):
        backbone_dict[check_list[1][j]] = pretrained_dict[check_list[0][j]]
    model_dict.update(backbone_dict)

    # check
    #for k in range((2 + 2 + 3 + 3 + 3) * 2):
    #   print((model_dict[model_dict.keys()[k]] == pretrained_dict[pretrained_dict.keys()[k]]).all())
    
    # save
    torch.save(model_dict, output_path)


if __name__ == '__main__':
    generate_VGG_16_model(Net.CTPN(), './model/vgg16.model')

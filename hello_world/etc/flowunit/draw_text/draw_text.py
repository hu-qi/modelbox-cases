# Copyright (c) Huawei Technologies Co., Ltd. 2022. All rights reserved.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 增加 opencv 和 numpy
import cv2
import numpy as np

import _flowunit as modelbox

class draw_textFlowUnit(modelbox.FlowUnit):
    # Derived from modelbox.FlowUnit
    def __init__(self):
        super().__init__()

    def open(self, config):
        # Open the flowunit to obtain configuration information
        return modelbox.Status.StatusCode.STATUS_SUCCESS

    def process(self, data_context):
        # Process the data
        in_data = data_context.input("in_1")
        out_data = data_context.output("out_1")

        # draw_text process code.
        # Remove the following code and add your own code here.
        # for buffer in in_data:
        for buffer_img in in_data:

            # 获取width、hight、channel
            width = buffer_img.get('width')
            height = buffer_img.get('height')
            channel = buffer_img.get('channel')

            # 处理图片
            img_data = np.array(buffer_img.as_object(), copy=False)
            img_data = img_data.reshape((height, width, channel))

            # 放置文本
            cv2.putText(img_data, 'Hello World', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # 输出
            out_buffer = self.create_buffer(img_data)
            out_buffer.copy_meta(buffer_img)
            out_data.push_back(out_buffer)

            # response = "Hello World " + buffer.as_object()
            # result = response.encode('utf-8').strip()
            # add_buffer = modelbox.Buffer(self.get_bind_device(), result)
            # out_data.push_back(add_buffer)

        return modelbox.Status.StatusCode.STATUS_SUCCESS

    def close(self):
        # Close the flowunit
        return modelbox.Status()

    def data_pre(self, data_context):
        # Before streaming data starts
        return modelbox.Status()

    def data_post(self, data_context):
        # After streaming data ends
        return modelbox.Status()

    def data_group_pre(self, data_context):
        # Before all streaming data starts
        return modelbox.Status()

    def data_group_post(self, data_context):
        # After all streaming data ends
        return modelbox.Status()
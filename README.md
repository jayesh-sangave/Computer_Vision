# Computer_Vision

## Convolution 
Convolution is a mathematical transformation that consists in multiplying two signals (one of the signals is reflected and shifted). To be more accurate, here is the mathematical continuous equation of a convolution of two functions f and g
![CONV_1_TRANSPARENT](https://github.com/user-attachments/assets/4c01d383-87c4-4cdf-81f8-a177ba7eb010)

`Note`  we won’t be using this convolution equation but rather the cross-correlation one. In fact, as it is the convention in computer vision.
![CONV_3_TRANSPARENT](https://github.com/user-attachments/assets/3e8c01d3-669f-43b6-8607-bdc87e4ebaf9)

![CONV_4](https://github.com/user-attachments/assets/7a7d1c08-3b4a-4fb3-8d35-f5bbf8df26a0)

## Convolution in Computer Vision

- Convolution is a fundamental operation in computer vision, especially in deep learning and image processing. It involves sliding a small matrix (called a kernel or filter) over an image to extract features like edges, textures, and patterns.

Mathematical Formula	

∑
𝑖
,
𝑗
(
Kernel
[
𝑖
,
𝑗
]
×
Image
[
𝑖
,
𝑗
]
)
∑ 
i,j
​
 (Kernel[i,j]×Image[i,j])

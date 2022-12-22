function y = ifft2c(x)
y = ifftshift(ifft2(ifftshift(x)));
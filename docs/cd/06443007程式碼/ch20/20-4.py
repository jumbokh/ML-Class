fig, axes = plt.subplots(4,4, figsize=(6,4))
for i, ax in enumerate(axes.flatten()):
    img = digit['data'][i].reshape(8, 8)
    ax.imshow(img, cmap='gray')
    ax.set_title(digit['target'][i])
    ax.axis('off')
plt.tight_layout()
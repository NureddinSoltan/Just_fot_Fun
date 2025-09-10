import cv2

def blur_score(image):
    """Compute Laplacian variance (sharpness measure)."""
    return cv2.Laplacian(image, cv2.CV_64F).var()

# Step 1: Load image
image = cv2.imread("normal.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


x, y, w, h = 100, 200, 300, 120  # Example dataplate ROI
dataplate = gray[y:y+h, x:x+w]

# Step 3: Blur detection only on the dataplate
score = blur_score(dataplate)

threshold = 120.0  # needs tuning
if score < threshold:
    print(f"Dataplate is blurry (score={score:.2f})")
else:
    print(f"Dataplate is sharp (score={score:.2f})")

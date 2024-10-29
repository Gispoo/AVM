import cv2
import time

# ������������� ������
cap = cv2.VideoCapture(0)

# �������� ���������� �������� ������
if not cap.isOpened():
  raise IOError("�� ������� ������� ������!")

# ������� �������������� (��������, ������� �� 90 ��������)
def transform_image(frame):
  return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

# ��������� �����������
fps_start_time = time.time()
frame_count = 0
while(True):
  ret, frame = cap.read()
  if not ret:
    break

  # �������������� �����������
  transformed_frame = transform_image(frame)

  # ����� ���������������� �����
  cv2.imshow('Video', transformed_frame)

  # ������� ������ � �������
  frame_count += 1
  if (time.time() - fps_start_time) > 1:
    fps = frame_count / (time.time() - fps_start_time)
    fps_start_time = time.time()
    frame_count = 0
    print(f"FPS: {fps}")

  # ����� �� ����� ��� ������� ������� 'q'
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# �������� ���� � ������������ ��������
cap.release()
cv2.destroyAllWindows()

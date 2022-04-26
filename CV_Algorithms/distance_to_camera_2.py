from fileinput import close
import yaml

with open(r'G:\LEGO\Bachelor_Lego\CV_Algoritms\camera.yaml') as file:

    # Loads camera properties from camera calibration
    data_load = yaml.load(file,Loader=yaml.FullLoader)

    # Loads Resolution size
    image_width = data_load.get("image_width")
    image_height = data_load.get("image_height")

    # Loads distortion type
    distortion_model = data_load.get("distortion_model")

    # Loads each matrix
    camera_matrix = data_load.get("camera_matrix").get("data")
    distortion_coefficients = data_load.get("distortion_coefficients").get("data")
    rectification_matrix = data_load.get("rectification_matrix").get("data")
    projection_matrix = data_load.get("projection_matrix").get("data")

    close() # ikke sikker på om den overhovedet gør det

# Extracting data to individual varibles
f_x = camera_matrix[0]
f_y = camera_matrix[2]
c_x = camera_matrix[4]
c_y = camera_matrix[5]

k_1 = distortion_coefficients[0]
k_2 = distortion_coefficients[1]
k_3 = distortion_coefficients[2]
k_4 = distortion_coefficients[3]
k_5 = distortion_coefficients[4]

# Below is a dummy value (units: mm)
focal_length = 5

# Read from data sheet
# (mm)
sensor_size_x = 5 
sensor_size_y = 3.7

m_x = image_width / focal_length
m_y = image_height / focal_length

 #distance_mm = object_real_world_mm * focal-length_mm / object_image_sensor_mm
#distance_mm = 70mm * 4.15mm / .308mm
#distance_mm = 943mm



print(camera_matrix)
print(c_y)

import python_terraform
import sys

tf = python_terraform.Terraform()

try:
    return_code, stdout, stderr = tf.apply(capture_output=False)
    print(f"Return code: {return_code}")
    print(f"Output: {stdout}")
    print(f"Errors: {stderr}")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

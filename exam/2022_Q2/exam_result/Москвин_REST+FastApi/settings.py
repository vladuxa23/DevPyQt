from minio import Minio

host = ""
a_key = ""
s_key = ""
secure_status = False

client = Minio(
    host,
    access_key=a_key,
    secret_key=s_key,
    secure=secure_status
)
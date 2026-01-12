docker run -dti \
  -p 5051:5055 \
  --ulimit nproc=4096 \
  --name flasklogin_run \
  -v /home/devasc/labs/tasks/Flask/flask_app_login/account_share:/home/app/data\
  flaskauth

FROM node:alpine
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter
# ENV PORT=7000
WORKDIR "/var/task"
ADD package.json /var/task/package.json
ADD package-lock.json /var/task/package-lock.json
RUN npm install --omit=dev
ADD . /var/task
CMD ["node", "index.js"]
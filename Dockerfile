FROM golang:alpine

WORKDIR /

COPY . .

EXPOSE 3000

RUN go install

RUN go build

CMD ["./ufc-stats-api"]

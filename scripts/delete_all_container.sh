for doc in `docker ps -a | grep -v CONTAINER | awk '{print $1}'`; do docker rm -f $doc; done

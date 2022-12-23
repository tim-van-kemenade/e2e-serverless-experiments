#!/bin/bash

echo -n "" > data/ff-overhead.txt

for i in {1..100} ; do
    curl -w "@curl-format.txt" -s "http://127.0.0.1:8080/function/floating-point-operation-sine" >> data/ff-overhead.txt
done

PODNAME=$(kubectl get pod -n openfaas-fn | sed -n "s/\(${podname}-[^ ]*\)\(.*\)/\1/gp" | tr '\n' ' ')
kubectl logs -n openfaas-fn $PODNAME > data/ff_pod_log.txt

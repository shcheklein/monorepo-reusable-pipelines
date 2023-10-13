#!/bin/bash
echo "Project/Model: $1"
echo "Target/Data/Customer: $2"

echo "Copy a $1:dvc.yaml template to pipeline: $1/$2"
cp $1/template_dvc.yaml $1/$2/dvc.yaml

echo "Run DVC pipeline: $1/$2"
dvc exp run -R $1/$2/dvc.yaml
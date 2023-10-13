#!/bin/bash
echo "PROJECT: $1"
echo "TARGET: $2"

split_on_commas() {
  local IFS=,
  local WORD_LIST=($1)
  for word in "${WORD_LIST[@]}"; do
    echo "$word"
  done
}

# Parse $2 comma separated list to get ${item} 
split_on_commas $2 | while read item; do
  
  # Run commands below for every ${item}
  echo "Project/Model: $1"
  echo "Target/Data/Customer: ${item}"

  echo "Copy a $1:dvc.yaml template to pipeline: $1/${item}"
  cp $1/template_dvc.yaml $1/${item}/dvc.yaml

  echo "Run DVC pipeline: $1/${item}"
  dvc exp run -R $1/${item}/dvc.yaml

done

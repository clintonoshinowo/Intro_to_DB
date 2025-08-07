#!/bin/bash

filename="$1"

if [ -s "$filename" ]; then
  echo "✅ Success: File '$filename' exists and is not empty."
else
  if [ -e "$filename" ]; then
    echo "⚠️ Warning: File '$filename' exists, but is empty."
  else
    echo "❌ Error: File '$filename' does not exist."
  fi
fi

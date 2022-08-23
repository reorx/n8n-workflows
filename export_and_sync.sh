#!/usr/bin/env bash

: ${EXPORT_DIR:="n8n-$(date +%Y%m%d)"}
: ${CONTAINER_NAME:="n8n-n8n-1"}
: ${EXPORT_HOST:="reorx@harrogath"}
: ${EXPORT_ROOT:="/share/CACHEDEV1_DATA/homes/reorx/Misc_Backup/"}
: ${DEST_DIR:=workflows}

download_dir=exports

set -eu

#docker exec -it -u node $CONTAINER_NAME node ./packages/cli/bin/n8n export:workflow --backup --output=/backup/$EXPORT_DIR/

rsync -ar ${EXPORT_HOST}:${EXPORT_ROOT}${EXPORT_DIR} $download_dir

python get_workflows.py $download_dir/$EXPORT_DIR $DEST_DIR

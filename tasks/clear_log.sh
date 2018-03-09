echo target_dir ${CLEAR_DIR}
for i in `find ${CLEAR_DIR} -name "*.log"`;
do
  echo clear $i;
  cat /dev/null > $i;
done
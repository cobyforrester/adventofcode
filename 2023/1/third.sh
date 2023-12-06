
total=0
while read l; do

  stripped=$(echo "$l" | sed 's/[^0-9]//g')
  length=${#stripped}
  count=$((count + 1))
  if [ $length == 1 ]; then
    stripped="$stripped$stripped"
    total=$((total + stripped))
  else
    first_num=${stripped:0:1}
    last_num=${stripped:0-1}
    num="$first_num$last_num"
    total=$((total + num))
  fi
done <./input.txt
echo $total
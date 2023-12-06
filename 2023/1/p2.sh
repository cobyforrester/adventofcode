
numbers=( one two three four five six seven eight nine )
total=0
while read line; do
  # pepper fixes of for all weird cases
  tampered=$(echo "$line" | sed 's/eighthree/eightthree/g'| sed 's/nineight/nineeight/g'| sed 's/oneight/oneeight/g'| sed 's/twone/twoone/g'| sed 's/eightwo/eighttwo/g'| sed 's/fiveight/fiveeight/g'| sed 's/sevenine/sevennine/g'| sed 's/sevenine/sevennine/g')
  for i in "${!numbers[@]}"; do 
    index=$(($i + 1))
    tampered=$(echo "$tampered" | sed "s/${numbers[$i]}/$index/g")
  done

  tampered=$(echo "$tampered" | sed 's/[^0-9]//g')
  length=${#tampered}
  if [ $length == 1 ]; then
    tampered="$tampered$tampered"
    total=$((total + tampered))
  else
    first_num=${tampered:0:1}
    last_num=${tampered:0-1}
    num="$first_num$last_num"
    echo "$num"
    total=$((total + num))
  fi
done <./input.txt
echo $total
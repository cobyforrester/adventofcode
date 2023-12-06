# FAILED ATTEMPT RAN OUT OF TIME

total=0
numbers=( one two three four five six seven eight nine )
while read l; do


  # find the first index of a number word
  # and the last index
  f_index=0
  f_value=""
  f_index=0
  f_value=""
  for key in "${numbers[@]}"
  do
    l_length=${#l}

    first=$(echo $l | sed "s/$key.*$//")
    first_index=${#first}

    rev_l=$(echo $l | rev)
    rev_key=$(echo $key | rev)

    last=$(echo $rev_l | sed "s/$rev_key.*$//")
    last_rev_index=${#last}
    last_index=$((l_length - last_rev_index))
  done
  
  echo $formatted
#   length=${#formatted}
#   if [ $length == 1 ]; then
#     formatted="$formatted$formatted"
#     total=$((total + formatted))
#   else
#     first_num=${formatted:0:1}
#     last_num=${formatted:0-1}
#     num="$first_num$last_num"
#     total=$((total + num))
#   fi
done <./input.txt
echo $total
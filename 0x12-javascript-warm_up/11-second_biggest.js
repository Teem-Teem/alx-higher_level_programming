#!/usr/bin/node

let argv = process.argv;

if (argv.length < 4) { console.log(0); } else {

  argv = argv.slice(2);

  let nums = argv.map(x => parseInt(x));
  nums = nums.sort(function (a, b) { return a - b; });

  console.log(nums[nums.length - 2]);
}

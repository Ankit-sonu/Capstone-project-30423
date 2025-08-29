const numbers = [10,20,30,40,50];
for(let x in numbers){
	console.log(x)
}

for(let x of numbers)
    console.log(x)

const nums = [1,2,3,4,5,6,7,8,9,10]
result = nums.map(n=>n*n);
console.log(result)

const evens = nums.filter(n => n%2 === 0)
console.log(evens)


result = nums.filter(n => n%2 === 0).map(x => x*x);
console.log("First Filter and Map :"+result)

result = nums.map(x => x*x).filter(n => n%2 === 0)
console.log("First Map and then Filter"+result)

console.log("The sum of first 10 numbers are : "+ nums.reduce((a,b)=>a+b),0)

const data = [10,20,1,2,200,97]
max = data.reduce((a,b)=>  a>b?a:b)

console.log("The maximum of "+max)

let today = new Date()
console.log(today)

console.log(nums.find(n => n%5==0))

let names = ["Hari","Sunil","Krishna"]
console.log(names.sort((a,b) => a.localeCompare(b)))
console.log(nums.sort((a,b)=>b-a))


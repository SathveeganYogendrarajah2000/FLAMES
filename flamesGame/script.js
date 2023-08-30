document.getElementById("play-button").addEventListener("click", function () {
  const name1 = document.getElementById("he-input").value.toLowerCase();
  const name2 = document.getElementById("she-input").value.toLowerCase();

  let n1 = [...name1];
  let n2 = [...name2];

  for (let i of name1) {
    if (n2.includes(i)) {
      n1.splice(n1.indexOf(i), 1);
      n2.splice(n2.indexOf(i), 1);
    }
  }

  let count = n2.length + n1.length;
  let word = ["F", "L", "A", "M", "E", "S"];

  while (word.length !== 1) {
    count = n2.length + n1.length;
    while (count > word.length) count -= word.length;
    word.splice(count - 1, 1);
    word = word.slice(count - 1).concat(word.slice(0, count - 1));
  }

  let result = "";
  switch (word[0]) {
    case "F":
      result = "Friends";
      break;
    case "L":
      result = "Love";
      break;
    case "A":
      result = "Affection";
      break;
    case "M":
      result = "Marriage";
      break;
    case "E":
      result = "Enemy";
      break;
    case "S":
      result = "Sister";
      break;
    default:
      result = "Result";
  }

  document.getElementById("result").textContent = result.toUpperCase();
});

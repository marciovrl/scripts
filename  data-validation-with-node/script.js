"use strict";

console.log("- Iniciando ...");

const xlsx = require("xlsx");

let request = require("request");

console.log("- Criando resultado.txt ....");
let fs = require("fs");
let txt = fs.createWriteStream("resultado.txt");

console.log("- Lendo dados.xlxs .....");
const workbook = xlsx.readFile("dados.xlsx");
const worksheet = workbook.Sheets[workbook.SheetNames[0]];

let url = "http://localhost:8080/example";

function chamando_api(dado, z) {
  return request(url + dado, function(error, response, body) {
    try {
      let result = JSON.parse(body);
      txt.write(
        "Linha planilha: " +
          z +
          " - Dado: " +
          dado +
          " Código Retorno: " +
          result.cod_retorno +
          " = Info 01: " +
          result.ou_campo_um +
          " Info 02: " +
          result.u_campo_um +
          "\n"
      );
    } catch (e) {
      chamando_api(dado, z);
    }
  });
}

function ler_planilha() {
  for (let z in worksheet) {
    if (z.toString()[0] === "A") {
      chamando_api(worksheet[z].v, z);
    }
  }
}

console.log("- Executando Consulta dos dados ......");
try {
  ler_planilha();
} catch (e) {
  console.log("Erro ao executar: " + e);
}

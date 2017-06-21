export const createImplication = (lhs: string, rhs: string) => {
  return "(" + lhs + ")" + " -> " + "(" + rhs + ")";
};

export const replaceConstWithVar = (text: string, variable: string, constant: string) => {
  console.error(text);
  console.error(variable);
  console.error(constant);
  const newText = text.replace(new RegExp(constant, "g"), "?" + variable);
  return "Forall ?" + variable + "(" + newText + ")";

};

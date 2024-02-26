Hor_t,Valor_hor,ret_F=48,5000,0.125;
Salario_bruto=Hor_t*Valor_hor;
Retencion=Salario_bruto*ret_F;
SalarioNeto=Salario_bruto*(1-ret_F);
print("Elsalario bruto es {}, la retencion es {} y el salario neto es {}".format(Salario_bruto,Retencion,SalarioNeto));



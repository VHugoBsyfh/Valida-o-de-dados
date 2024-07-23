from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta")


class DocCpf:

    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def validar(self, documento):
        valida = CPF()
        return valida.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def validar(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def format(self):
        formatar = CNPJ()
        return formatar.mask(self.cnpj)

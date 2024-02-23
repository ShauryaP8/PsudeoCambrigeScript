if __name__ == "__main__":
    # cli()
    from cambridgeScript.parser.lexer import parse_tokens
    from cambridgeScript.parser.parser import Parser
    from cambridgeScript.interpreter.variables import VariableState
    from cambridgeScript.interpreter.interpreter import Interpreter

    tokens = parse_tokens(open(0).read())
    for token in tokens:
        print(token)
    parsed = Parser.parse_program(tokens)
    print(parsed)
    interpreter = Interpreter(VariableState())
    interpreter.visit(parsed)
from core.lexer import Lexer, TokenType

code = """
var x = 10;
fn main() {
    if (x == 10) {
        x = x + 1;
    }
}
"""

lexer = Lexer(code)
try:
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
except Exception as e:
    print(f"Lexer Error: {e}")
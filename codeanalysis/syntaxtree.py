from typing import List
from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.syntaxtoken import SyntaxToken


class SyntaxTree:
    def __init__(
        self,
        diagnostics: List[str],
        root: ExpressionSyntax,
        end_of_file_token: SyntaxToken,
    ) -> None:
        self.diagnostics = diagnostics
        self.root = root
        self.end_of_file_token = end_of_file_token


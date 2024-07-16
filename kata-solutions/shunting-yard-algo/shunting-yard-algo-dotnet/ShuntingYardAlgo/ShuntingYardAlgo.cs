using System;
using System.Text.RegularExpressions;

namespace InfixToPostfix;

public class ShuntingYardAlgo
{
    private string _result = "";
    private string _previousToken = "";
    private string[] _tokens = new String[] { ""};

    public string Transform(string expression)
    {
        Initialize(expression);

        ProcessTokens();

        return _result;
    }

    private void ProcessTokens() 
    {
        foreach(string current in _tokens)
            if (IsLiteral(current))
                HandleLiteral(current);
            else
                HandleOperator(current);
    
        AppendToken(_previousToken);
    }

    private void HandleOperator(string token)
    {
        AppendToken(_previousToken); 
        _previousToken = token;
    }

    private void Initialize(string expression)
    {
        _tokens = (expression ?? "").Split(" ");
        _previousToken = "";
        _result = "";

    }

    private void HandleLiteral(string literal) => AppendToken(literal);

    private void AppendToken(string token)
    {
        if (_result.Length > 0 && token.Length > 0)
            _result += " ";

        _result += token;
    }
    private bool IsLiteral(string token) => Regex.IsMatch(token, @"(\w+|\d+)");
}

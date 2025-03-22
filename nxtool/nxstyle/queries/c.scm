; function definitions and body
(function_definition
    
    (storage_class_specifier)?
    type: (primitive_type)
    declarator: (function_declarator)
    body: (compound_statement) @function.body
)

(parenthesized_expression) @expression.paranthesis

(argument_list) @list.arguments

(struct_specifier) @structs
(enum_specifier) @enums

(declaration
	_+
	(pointer_declarator)
) @declarator.pointer

(cast_expression) @declarator.pointer

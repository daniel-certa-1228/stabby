CREATE OR REPLACE FUNCTION url_encode(input_text text)
RETURNS text AS $$
DECLARE
    output_text text := '';
    char text;
    hex_char text;
BEGIN
    -- Loop through each character in the input text
    FOR char IN SELECT unnest(string_to_array(input_text, NULL)) LOOP
        -- Check if the character is alphanumeric or a safe character
        IF char ~ '^[a-zA-Z0-9._~-]$' THEN
            output_text := output_text || char;
        ELSE
            -- Convert character to its hex representation and prepend with '%'
            hex_char := '%' || upper(lpad(to_hex(ascii(char)), 2, '0'));
            output_text := output_text || hex_char;
        END IF;
    END LOOP;
    RETURN output_text;
END;
$$ LANGUAGE plpgsql;



// Functions for validations:
const isValidUsername = (username) => {
    const regex = /^[a-zA-Z0-9_@.+\\-]{3,25}$/; // This regex requires the username to have at least 3 characters and only allow letters, numbers, dots, underscores, and hyphens.
    return regex.test(username); // Test is a built-in function in JavaScript used to test if a given string matches a regular expression
}

const isValidPassword = (password) => {
    const regex = /^(?=.*[a-zA-Z0-9])(?=.*[-+.@_])[a-zA-Z0-9-+.@_]{8,}$/;
    return regex.test(password);
}

export { isValidUsername, isValidPassword }
  
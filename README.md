# btd6-aliases

This repository acts as a hub for BTD6 Game Object aliases.

## How to Use

GitHub hosts the raw data version of every file in a repository. We can use that link as a way to fetch the JSON objects for these aliases.

In your programming language of choice, fetch the link and deserialize the JSON.

## Suggesting an Edit

I recommend the following methods for suggesting edits:

1. Create a Pull Request (best)

   - Create a Pull Request with your edits and a repository owner/moderator will act accordingly.

2. Submit a GitHub Issue
   - Submit an issue and suggest the alias and which Game Object it should be associated with. Then the request will be reviewed.

> [!IMPORTANT]
> Alias requests are not guaranteed to be approved or accepted.

## Partnered Projects

- [ChatPlaysBTD6](https://github.com/oatsfx/ChatPlaysBTD6)

## Stuff for Nerds

Every JSON object is a Dictionary following this format:

```json
{ "<T>": ["<ALIAS_1>", "<ALIAS_2>", "<ALIAS_n>"] }
```

- where `T` is a generic for the game object type. They are commonly strings, but things like path indexes need integers.
- where `ALIAS_n` is an arbitrary string marking an infinite list of aliases.

The game objects are classified into separate files according to the type of object they are (i.e. abilities, towers, target types).

We have a script that will check for duplicates on pushes and pull requests. Duplicates are not allowed within the same file, but are allowed across files.

Thanks for reading.

// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// To keep track of how many words are in the dictionary
int word_count = 0;


// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table into the very beginning of each bucket
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));

        // Check if enough memory
        if (new_node == NULL)
        {
            unload();
            return false;
        }

        // Copy new word into node
        strcpy(new_node->word, word);

        // Run through hash function, give bucket number
        int bucket = hash(word);

        // If no nodes/words in bucket, put address to node in the hash table
        new_node->next = hashtable[bucket];

        // If there already is, then point the new node to what the previous node was pointing to
        hashtable[bucket] = new_node;

        // Update how many words are in the dictionary
        word_count ++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (&load)
    {
        return word_count;
    }
    else
    {
        return 0;
    }
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Finds which bucket the word would be in
    int bucket_for_check = hash(word);
    node *cursor = hashtable[bucket_for_check];

    // Return true if the word is in the dictionary
    if (hashtable[bucket_for_check])
    {
        // Traverse the linked list until its end
        while (cursor != NULL)
        {
            // See if the word is in the dictionary
            if (strcasecmp(cursor->word, word) == 0)
            {
                return true;
            }
            else
            {
                cursor = cursor->next;
            }
        }
    }
    // If the word is not in the dictionary then return false
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Iterates over each bucket of the hashtable
    for (int i = 0; i < 26; i++)
    {
        node *cursor = hashtable[i];

        // Free memory in each element of the linked list
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    // Successfully unloaded
    return true;
}

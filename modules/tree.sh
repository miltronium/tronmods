#!/bin/bash

# Function to print directory tree recursively
print_tree() {
    local dir="${1:-.}"
    local prefix="${2}"
    local depth="${3:-0}"
    local max_depth="${4:-999}"

    # Check if max depth is reached
    if [ "$depth" -ge "$max_depth" ]; then
        return
    fi

    # Get all items in the directory
    local items=()
    local count=0

    # Use find to get immediate children only
    while IFS= read -r -d '' item; do
        items+=("$item")
        ((count++))
    done < <(find "$dir" -maxdepth 1 -mindepth 1 -print0 2>/dev/null | sort -z)

    # Process each item
    local i=0
    for item in "${items[@]}"; do
        ((i++))
        local basename=$(basename "$item")

        # Determine if this is the last item
        if [ "$i" -eq "$count" ]; then
            echo "${prefix}└── $basename"
            local new_prefix="${prefix}    "
        else
            echo "${prefix}├── $basename"
            local new_prefix="${prefix}│   "
        fi

        # If it's a directory, recurse
        if [ -d "$item" ]; then
            print_tree "$item" "$new_prefix" $((depth + 1)) "$max_depth"
        fi
    done
}

# Main script
main() {
    local target_dir="${1:-.}"
    local max_depth="${2:-999}"

    # Check if directory exists
    if [ ! -d "$target_dir" ]; then
        echo "Error: '$target_dir' is not a valid directory"
        exit 1
    fi

    # Print the root directory
    echo "$(basename "$(realpath "$target_dir")")"

    # Print the tree
    print_tree "$target_dir" "" 0 "$max_depth"
}

# Show usage if --help is passed
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: $0 [directory] [max_depth]"
    echo "  directory: Path to directory (default: current directory)"
    echo "  max_depth: Maximum depth to traverse (default: unlimited)"
    echo ""
    echo "Example: $0 /home/user/projects 3"
    exit 0
fi

# Run the main function
main "$@"
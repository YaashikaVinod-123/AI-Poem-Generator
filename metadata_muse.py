from PIL import Image
from PIL.ExifTags import TAGS

# Get image path from user
image_path = input("Enter the full path to your image file (e.g., C:\\Users\\HP\\Pictures\\image.jpg): ")

try:
    # Open the image
    image = Image.open(image_path)
    metadata = image._getexif()

    # Check if metadata is found
    if metadata:
        print("Metadata found! Here it is:")
        for tag_id, value in metadata.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")  # Print each metadata tag and its value

        # Use metadata to generate a poem
        poem = f"""
        This image tells a tale of time,
        Captured in {metadata.get(36867, 'a moment unknown')},
        A snapshot of light, a fleeting climb,
        Echoing stories never outgrown.
        """
        print("\nGenerated Poem:\n")
        print(poem)
    else:
        print("No metadata found for this image. Try another image.")
except FileNotFoundError:
    print("The file was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")


def generate_poem(metadata):
    """
    Generates a short poem based on extracted metadata.
    """
    lines = []

    # Use specific metadata keys if available
    if 'Make' in metadata:
        lines.append(f"A masterpiece born of {metadata['Make']},")
    if 'Model' in metadata:
        lines.append(f"Captured through the lens of {metadata['Model']}.")
    if 'DateTime' in metadata:
        lines.append(f"On a day etched in time: {metadata['DateTime']},")
    if 'FNumber' in metadata:
        lines.append(f"With precision so sharp, f/{metadata['FNumber']} was the rhyme.")
    if 'ExposureTime' in metadata:
        lines.append(f"The light danced for {metadata['ExposureTime']} seconds.")

    # Add fallback lines if metadata is limited
    if not lines:
        lines.append("An image speaks a thousand words,")
        lines.append("Yet its story is untold, unheard.")

    # Add a closing line
    lines.append("Art frozen in time, forever divine.")

    return "\n".join(lines)

def main():
    print("=== Welcome to Metadata-to-Poem Generator ===")

    # Ask the user for the image file path
    image_path = input("\nEnter the full path to your image file (e.g., C:\\Users\\HP\\Pictures\\image.jpg): ").strip()

    if not os.path.exists(image_path):
        print("\nError: The specified file does not exist. Please check the path and try again.")
        return

    # Extract metadata
    metadata = extract_metadata(image_path)
    if metadata:
        # Generate and display the poem
        print("\nHere is your generated poem:\n")
        poem = generate_poem(metadata)
        print(poem)

        # Ask the user if they want to save the poem
        save_choice = input("\nDo you want to save this poem to a file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            output_file = input("\nEnter the desired name for the poem file (e.g., metadata_poem.txt): ").strip()
            try:
                with open(output_file, "w") as file:
                    file.write(poem)
                print(f"\nPoem saved successfully to {output_file}")
            except Exception as e:
                print(f"\nError: Unable to save the poem. Reason: {e}")
        else:
            print("\nPoem not saved. Exiting the program.")
    else:
        print("\nNo metadata to process. Exiting the program.")

if __name__ == "__main__":
    main()

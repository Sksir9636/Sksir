import pyrogram
import requests

# Create a Pyrogram Client
app = pyrogram.Client("Url_sirjibot")

# Handler for the /start command
@app.on_message(pyrogram.Filters.command("start"))
def start(bot, update):
    # Send a message asking for the TXT file
    bot.send_message(update.chat.id, "Please send me the TXT file.")

# Handler for receiving the TXT file
@app.on_message(pyrogram.Filters.document)
def receive_txt(bot, update):
    # Download the TXT file
    file = bot.get_file(update.document.file_id)
    file.download("txt_file.txt")

    # Read the TXT file and count the number of links
    with open("txt_file.txt", "r") as f:
        links = f.readlines()
    
    num_links = len(links)

    # Send the total number of links to the user
    bot.send_message(update.chat.id, f"Total links found in this txt file: {num_links}")

    # Ask for the download source
    bot.send_message(update.chat.id, "Send from where you want to download. Initial is 0.")

# Handler for receiving the download source
@app.on_message(pyrogram.Filters.text)
def receive_source(bot, update):
    # Get the download source index from user input
    source_index = int(update.text)

    # Ask for the batch name
    bot.send_message(update.chat.id, "Please enter the batch name.")

# Handler for receiving the batch name
@app.on_message(pyrogram.Filters.text)
def receive_batch_name(bot, update):
    # Get the batch name from user input
    batch_name = update.text

    # Ask for the resolution
    bot.send_message(update.chat.id, "Please enter the resolution.")

# Handler for receiving the resolution
@app.on_message(pyrogram.Filters.text)
def receive_resolution(bot, update):
    # Get the resolution from user input
    resolution = update.text

    # Ask for the thumbnail URL
    bot.send_message(update.chat.id, "Please enter the thumbnail URL. (Eg: https://telegra.ph/file/xxx.jpg)")

# Handler for receiving the thumbnail URL
@app.on_message(pyrogram.Filters.text)
def receive_thumbnail_url(bot, update):
    # Get the thumbnail URL from user input
    thumbnail_url = update.text

    # Ask if user wants to proceed with the download
    bot.send_message(update.chat.id, "Send 'yes' to start the download or 'no' to cancel.")

# Handler for starting the download
@app.on_message(pyrogram.Filters.text)
def start_download(bot, update):
    # Check if user wants to proceed with the download
    if update.text.lower() == "yes":
        # Download the videos and PDFs from the TXT file
        with open("txt_file.txt", "r") as f:
            links = f.readlines()
        
        num_videos = 0
        num_pdfs = 0

        for link in links:
            link = link.strip()  # Remove any leading/trailing whitespace
            
            if link.endswith(".mp4"):
                # Download the video
                response = requests.get(link)
                with open(f"{batch_name}_{num_videos}.mp4", "wb") as f:
                    f.write(response.content)
                
                num_videos += 1
            
            elif link.endswith(".pdf"):
                # Download the PDF
                response = requests.get(link)
                with open(f"{batch_name}_{num_pdfs}.pdf", "wb") as f:
                    f.write(response.content)
                
                num_pdfs += 1
        
        # Send the download summary to the user
        bot.send_message(update.chat.id, f"Download complete. Total videos: {num_videos}, Total PDFs: {num_pdfs}")
    
    else:
        # Cancel the download
        bot.send_message(update.chat.id, "Download canceled.")

# Start the bot
app.run()

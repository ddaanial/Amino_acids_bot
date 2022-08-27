import telegram.ext

token = '5673931415:AAEsWemOnA3PXLN8CjUu4JZ7Hrdjro3vA30'

def start(update, context):
    update.message.reply_text("""
    Wellcome to AminoAcidsWorld!

/help -> for help
    """)


def txt(update, context):
    try:
        update.message.reply_photo(photo=open(f'images/{update.message.text}.png', 'rb'))
    except:
        update.message.reply_text("""
Not valid name.

Try again!
    """)

def help_handle(update, context):
    update.message.reply_text("""
Give me name of the amino acid to get it's structure:

List of Amino Acids:
alanine
arginine
asparagine
aspartic_acid
cysteine
glutamic_acid
glutamine
glycine
histidine
isoleucine
leucine
lysine
methionine
phenylalanine
proline
serine
threonine
tryptophan
tyrosine
valine
    """)


updater = telegram.ext.Updater(token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help_handle))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, txt))


updater.start_polling()
updater.idle()
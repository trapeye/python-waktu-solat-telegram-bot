from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon=JHR03')

xml = BeautifulSoup(req,'xml')
for kluang in xml.findAll('description')[:1]:
#    print(kluang.text)

    for imsak in xml.findAll('description')[1:2]:
    #    print(imsak.text)

        for subuh in xml.findAll('description')[2:3]:
        #    print(subuh.text)

            for syuruk in xml.findAll('description')[3:4]:
            #    print(syuruk.text)

                for zohor in xml.findAll('description')[4:5]:
                #    print(zohor.text)

                    for asar in xml.findAll('description')[5:6]:
                    #    print(asar.text)

                        for maghrib in xml.findAll('description')[6:7]:
                        #    print(maghrib.text)

                            for isyak in xml.findAll('description')[7:8]:
                            #    print(isyak.text)

                                import logging

                                from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

                                logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                                    level=logging.INFO)

                                logger = logging.getLogger(__name__)



                                def start(update, context):
                                    update.message.reply_text('Hi awak hehehehehhe ini adalah starter!')


                                def help(update, context):
                                    update.message.reply_text('aku robot aku tak tau help itu apa, cer taip or tekan ni --> /solat')

                                def solat(update, context):
                                    update.message.reply_text("WAKTU SOLAT DI "+kluang.text+"\n"+
                                                              "(24hour)"+"\n\n"+
                                                              "Imsak:    "+imsak.text+"\n\n"+
                                                              "Subuh:    "+subuh.text+"\n\n"+
                                                              "Syuruk:   "+syuruk.text+"\n\n"+
                                                              "Zohor:     "+zohor.text+"\n\n"+
                                                              "Asar:       "+asar.text+"\n\n"+
                                                              "Maghrib: "+maghrib.text+"\n\n"+
                                                              "Isyak:       "+isyak.text)


                                def echo(update, context):
                                    update.message.reply_text(update.message.text)


                                def error(update, context):
                                    logger.warning('Update "%s" caused error "%s"', update, context.error)


                                def main():
                                    updater = Updater("TOKEN", use_context=True)

                                    dp = updater.dispatcher

                                    dp.add_handler(CommandHandler("start", start))
                                    dp.add_handler(CommandHandler("help", help))
                                    dp.add_handler(CommandHandler("solat", solat))

                                    dp.add_handler(MessageHandler(Filters.text, echo))

                                    dp.add_error_handler(error)

                                    updater.start_polling()

                                    updater.idle()


                                if __name__ == '__main__':
                                    main()









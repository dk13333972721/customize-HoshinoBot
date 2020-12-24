import hoshino
import nonebot
from nonebot import scheduler
from nonebot import on_command, CommandSession
from hoshino import log, priv, Service
from .data_source import Check

MAX_PERFORMANCE_PERCENT = hoshino.config.check.MAX_PERFORMANCE_PERCENT
PROCESS_NAME_LIST = hoshino.config.check.PROCESS_NAME_LIST

logger = log.new_logger('check')
check = Check(hoshino.config.check.PROCESS_NAME_LIST)

sv = Service('check', use_priv=priv.SUPERUSER, manage_priv=priv.SUPERUSER, visible=False) 

@sv.on_fullmatch(('自检','自我检查'))
async def self_check(bot, event):
    if not priv.check_priv(event, priv.SUPERUSER):
        return
    check_report_admin = await check.get_check_info()
    if check_report_admin:
        await bot.send(event, check_report_admin)
    else:
        logger.error("Not found Check Report")
        await event.send(bot, "[ERROR]No Check Report")


#@scheduler.scheduled_job('cron', hour='*/3', minute='13') 
async def check_task():
    bot = nonebot.get_bot()
    weihu = hoshino.config.SUPERUSERS[0]
    result = await check.get_check_easy()        
    await bot.send_private_msg(user_id=weihu, message=result)

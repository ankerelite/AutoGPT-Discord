from typing import TypedDict
import json
import discord

class Message(TypedDict):
    role: str
    content: any
    
def autoGPTMessageEmbed(message: Message) -> discord.Embed:
    """
    Message embedding
    """
    if(message["role"] == "ON_BOOT"):
        embed=discord.Embed(title=translateType(message["role"]),url="https://github.com/gravelBridge/AutoGPT-Discord",description="AutoGPT Discord Bot just woke up. Hello! Give me a moment to get my things arranged...",color=translateTypeColor(message["role"]))
        embed.set_author(name="gravelBridge", url="https://github.com/gravelBridge/AutoGPT-Discord", icon_url="https://avatars.githubusercontent.com/u/107640947?v=4")
        embed.set_thumbnail(url="")
    else:
        embed=discord.Embed(title=translateType(message["role"]),url="",description="",color=translateTypeColor(message["role"]))
        embed.set_author(name="", url="", icon_url="")
        embed.set_thumbnail(url="")

    try:
        parsed = json.loads(message["content"])
        
        if message["role"] == "ON_RESPONSE":
            """
            Base AutoGPT response formatter
            """
            
            embed.add_field(name=bold("Thoughts:"), value=parsed["thoughts"]["text"], inline=False)
            embed.add_field(name=bold("Reasoning:"), value=parsed["thoughts"]["reasoning"], inline=False)
            embed.add_field(name=bold("Plan:"), value=parsed["thoughts"]["plan"], inline=False)
            embed.add_field(name=bold("Criticism:"), value=parsed["thoughts"]["criticism"], inline=False)
            embed.add_field(name=bold("Command Name:"), value=parsed["command"]["name"], inline=False)

            command_args = parsed["command"]["args"]
            msg = ""
            for key, value in command_args.items():
                msg += f"{key}: {italic(value)}\n"
            
            embed.add_field(name=bold("Command Args:"), value=msg, inline=False)
            
            color=translateTypeColor(message["role"])

        elif message["role"] == "REQUEST":
            """
            Base AutoGPT request formatter
            """

            embed.add_field(name=bold("Action:"), value=f"I want to run {italic(parsed['name'])} command with the following arguments:", inline=False)

            command_args = parsed["args"]
            msg = ""
            for key, value in command_args.items():
                msg += f"{key}: {italic(value)}\n"
            
            embed.add_field(name="", value=msg, inline=False)
            embed.add_field(name=bold("Options:"), value=f" - {bold('y')} to allow\n - {bold('n')} to refuse\n - {bold('give feedback')} to change current plan", inline=False)
            
            color=translateTypeColor(message["role"])

        
        #TODO: Add other message types support
        else:
           embed.add_field(name="", value=message["content"], inline=False)
           color=translateTypeColor(message["role"])

    except:
        embed.add_field(name="", value=message["content"], inline=False)
        color=translateTypeColor(message["role"])
    
    return embed

def parsingErrorEmbed() -> discord.Embed:
    """
    Parsing error embedding
    """
    embed=discord.Embed(title= "A Moment of Mindfulness",url="",description="",color=discord.Color.orange())
    embed.set_author(name="", url="", icon_url="")
    embed.set_thumbnail(url="")
    embed.add_field(name="", value="Quite a large amount of data, I see. Please hold...", inline=False)

    return embed

def shutdownEmbed(message: str) -> discord.Embed:
    """
    Shutdown embedding
    """
    embed=discord.Embed(title= "Adios!",url="https://github.com/CTHULHUCTHULHU/AutoGPT-Discord",description="",color=discord.Color.red())
     embed.set_author(name="CTHULHUCTHULHU", url="https://github.com/CTHULHUCTHULHU/AutoGPT-Discord", icon_url="https://avatars.githubusercontent.com/u/134018141?v=4")
    embed.set_thumbnail(url="")
    embed.add_field(name="", value=message, inline=False)

    return embed

#TODO: There has to be better mapping than this shit
def translateType(message: str) -> str:
    if(message == "ON_RESPONSE"):
        return "Summary"
    elif(message == "ON_BOOT"):
        return "Welcome!"
    elif(message == "REQUEST"):
        return "Request"
    elif(message == "POST_PLANNING"):
        return "Post Planning"
    elif(message == "POST_INSTRUCTION"):
        return "Post Instruction"
    elif(message == "POST_COMMAND"):
        return "Reply"
    elif(message == "REQUEST_INPUT"):
        return "Request Input"
    elif(message == "REPORT"):
        return "Report"
    elif(message == ""):
       return "Unknown Source"
    else:
        return message
        
#TODO: There has to be better mapping than this shit
def translateTypeColor(message: str) -> str:
    if(message == "ON_RESPONSE"):
        return discord.Color.purple()
    elif(message == "ON_BOOT"):
        return discord.Color.green()
    elif(message == "REQUEST"):
        return discord.Color.yellow()
    elif(message == "POST_PLANNING"):
        return discord.Color.orange()
    elif(message == "POST_INSTRUCTION"):
        return discord.Color.purple()
    elif(message == "POST_COMMAND"):
        return discord.Color.blue()
    elif(message == "REQUEST_INPUT"):
        return discord.Color.blue()
    elif(message == "REPORT"):
        return discord.Color.blue()
    elif(message == ""):
       return discord.Color.purple()
    else:
        return message

def italic(txt):
    return '*' + txt +'*'

def bold(txt):
    return '**' + txt +'**'

def underline(txt):
    return '__' + txt +'__'

def strike(txt):
    return '~~' + txt +'~~'

def sl_blockquote(txt):
    return '\n> {}'.format(txt)

def ml_blockquote(txt):
    return '\n> {}'.format(txt)

def sl_code(txt):
    return '`' + txt + '`'

def ml_code(txt):
    return '```' + txt + '```'
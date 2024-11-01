import os
import logging
import traceback
import datetime


def get_logger(LEVEL: str = "INFO") -> logging.Logger:
    # log_time = datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")

    logger = logging.getLogger("custom_logger")
    logger.setLevel(getattr(logging, LEVEL.upper(), logging.INFO))

    # file_handler = logging.FileHandler(f"./logs/{log_time}_logfile.log")
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="[%(asctime)s %(levelname)s] %(message)s", datefmt="%Y/%m/%d %H:%M:%S"
    )
    # file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    # logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def sol(problem_num, func):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = script_dir + f"\\txt\\{problem_num}" + ".txt"
    logger.info(f"file path : {path}")

    try:
        with open(path, "r") as getter:
            line_count = 1
            while True:
                line = getter.readline()
                # logger.info(f"this line : {line.strip().split()}")
                if not line:
                    logger.info("EOF")
                    break
                try:
                    inp, oup = line.strip().split()
                    if not func(inp):
                        raise ValueError(f"wrong output in line : {line}")
                    logger.info(f"{line_count} : {inp} : {oup == func(inp)}")
                    line_count += 1
                except Exception as e:
                    logger.error(f"Error occurred while processing line: {line}")
                    logger.error(f"Exception: {e}")
                    logger.error(traceback.format_exc())
                    line_count += 1
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
    except Exception as e:
        logger.error(f"Error opening file: {e}")
        logger.error(traceback.format_exc())
    logger.info("ACCEPT")


class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""

        grouped = []
        current_group = s[0]
        for char in s[1:]:
            if char == current_group[-1]:
                current_group += char
            else:
                grouped.append(current_group)
                current_group = char
        grouped.append(current_group)

        for group in grouped:
            if len(group) > 2:
                result += group[0] * 2
            else:
                result += group

        return result


problem_num = 1957
global logger
logger = get_logger("info")
sol(problem_num, Solution().makeFancyString)

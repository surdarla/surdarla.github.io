import os
import logging
import traceback


def get_logger() -> logging.Logger:
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=logging.INFO,
    )
    logger = logging.getLogger()
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
                    logger.info(f"{line_count} : {inp} : {int(oup) == func(inp)}")
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
    def maxUniqueSplit(self, s: str) -> int:
        sett = set()

        def dfs(s):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                if s[:i] not in sett:
                    sett.add(s[:i])
                    res = max(res, 1 + dfs(s[i:]))
                    sett.remove(s[:i])
            return res

        return dfs(s)


problem_num = 1593
global logger
logger = get_logger()
sol(problem_num, Solution().maxUniqueSplit)

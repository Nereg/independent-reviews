import aiogram.utils.formatting as fmt

from sql.reviews import getReviewByIdRow, getReviewsByIdsRow

REVIEW_ROW = getReviewByIdRow | getReviewsByIdsRow
from commons import Faculty


def star_rating(rating: int) -> str:
    match rating:
        case 0:
            return "☆☆☆☆☆"
        case 1:
            return "★☆☆☆☆"
        case 2:
            return "★★☆☆☆"
        case 3:
            return "★★★☆☆"
        case 4:
            return "★★★★☆"
        case 5:
            return "★★★★★"
        case _:
            raise ValueError("Rating can only be 0-5!")


def commonLayout(
    inputObj: REVIEW_ROW,
) -> fmt.Text:  # every other element is based on text
    """
    Constructs a common layout to be used while displaying a review
    """
    result = fmt.as_list(
        fmt.BlockQuote(
            fmt.as_list(
                fmt.Bold(f"Review №{inputObj.id}"),
                fmt.as_line(
                    "Review faculty: ",
                    fmt.Bold(Faculty(inputObj.facultyId).name),
                    end="",
                ),
                fmt.as_line(
                    "Review subject: ",
                    fmt.Bold(inputObj.name + " (" + inputObj.aisCode + ")"),
                    end="",
                ),
                fmt.as_line(
                    f"Review year: ",
                    fmt.Bold(
                        f"{str(inputObj.yearBeginning)}/{str(inputObj.yearBeginning+1)}"
                    ),
                    end="",
                ),
            )
        ),
        f"Subject rating: {star_rating(inputObj.subjectRating)}",
        fmt.as_line("Reviewer's mark: ", str(inputObj.mark), end=""),
        fmt.Bold("Review text:"),
        fmt.BlockQuote(inputObj.text),
    )
    return result

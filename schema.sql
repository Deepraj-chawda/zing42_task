DROP TABLE IF EXISTS equity;

CREATE TABLE equity (
    symbol VARCHAR PRIMARY KEY,
    name_of_company TEXT,
    series VARCHAR(2),
    date_of_listing DATE,
    paid_up_value INTEGER,
    market_lot INTEGER,
    isin_number VARCHAR,
    face_value INTEGER
);
CREATE TABLE bhavcopy(
    market VARCHAR,
    series VARCHAR,
    symbol VARCHAR PRIMARY KEY,
    security TEXT,
    prev_cl_pr FLOAT,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    net_trdval INTEGER,
    net_trdqty INTEGER,
    corp_ind VARCHAR,
    hi_52_wk FLOAT,
    lo_52_wk FLOAT


)

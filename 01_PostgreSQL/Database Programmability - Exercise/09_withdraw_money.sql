CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(8,4)
) AS
$$
BEGIN
    IF (SELECT balance FROM accounts WHERE account_id = accounts.id) >= money_amount THEN
        UPDATE accounts SET balance = balance - money_amount
        WHERE account_id = accounts.id;
    ELSE RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
    END IF;
END;
$$
LANGUAGE plpgsql;


-- CALL sp_withdraw_money(3, 5050.7500);
-- CALL sp_withdraw_money(6, 5437.0000);
-- 
-- SELECT * FROM accounts WHERE id = 3;





-- CREATE OR REPLACE PROCEDURE sp_withdraw_money(
-- 	account_id INT,
-- 	money_amount NUMERIC(10,4)
-- )
-- AS
-- $$
-- DECLARE	
-- 	curr_balance NUMERIC;
-- BEGIN
-- 	curr_balance := (SELECT balance FROM accounts WHERE id = account_id);
-- 	IF (curr_balance - money_amount) > 0 THEN
-- 		UPDATE accounts
-- 		SET balance = balance - money_amount 
-- 		WHERE account_id = accounts.id;
-- 	ELSE
-- 		RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
-- 	END IF;
-- END;
-- $$
-- LANGUAGE plpgsql;


-- CALL sp_withdraw_money(3, 5050.7500);
-- CALL sp_withdraw_money(6, 5437.0000);

-- SELECT * FROM accounts WHERE id = 3;

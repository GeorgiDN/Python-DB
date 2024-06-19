CREATE OR REPLACE PROCEDURE sp_transfer_money(
	sender_id INT,
	receiver_id INT,
	amount NUMERIC
)
AS
$$
DECLARE
	curr_balance NUMERIC;
BEGIN
	CALL sp_withdraw_money(sender_id, amount);
	CALL sp_deposit_money(receiver_id, amount);
	
	SELECT balance INTO curr_balance
	FROM accounts WHERE id = sender_id;
	
    IF (curr_balance) < 0 THEN
		ROLLBACK;
	END IF;
END;
$$
LANGUAGE plpgsql;

-- CALL sp_transfer_money(1, 1, 10.0000);
create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');

DROP TABLE IF EXISTS `sexo_interes`;
CREATE TABLE IF NOT EXISTS `sexo_interes` (
  `id_sex` int(3) NOT NULL,
  `nom_sex` varchar(20) NOT NULL,
  PRIMARY KEY (`id_sex`)
); 

INSERT INTO `sexo_interes` (`id_sex`, `nom_sex`) VALUES
(1, 'Mujeres'),
(2, 'Hombres'),
(3, 'Ambos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tip_usu`
--

DROP TABLE IF EXISTS `tip_usu`;
CREATE TABLE IF NOT EXISTS `tip_usu` (
  `id_tip_usu` int(11) NOT NULL,
  `nom_tip_usu` varchar(20) NOT NULL,
  PRIMARY KEY (`id_tip_usu`)
);
--
-- Volcado de datos para la tabla `tip_usu`
--

INSERT INTO `tip_usu` (`id_tip_usu`, `nom_tip_usu`) VALUES
(1, 'Premium'),
(2, 'Estandar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_tip_usu` int(11) NOT NULL,
  `interes` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tip_usu` (`id_tip_usu`),
  KEY `interes` (`interes`)
);
COMMIT;

